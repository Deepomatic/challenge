// include python.hpp before anything else
#include <boost/python.hpp>

#include <string>
#include <vector>
#include <iostream>

#include "checkers/ai.h"

namespace bp = boost::python;
using namespace std;
using namespace checkers;

struct BoardToCpp
{
    BoardToCpp()
    {
        boost::python::converter::registry::push_back(
            &convertible,
            &construct,
            boost::python::type_id<std::vector<std::string>>());
    }

    static void* convertible(PyObject* obj_ptr)
    {
        if (!PyList_Check(obj_ptr)) {
            return nullptr;
        }
        return obj_ptr;
    }

    static void construct(PyObject* obj_ptr,
                           boost::python::converter::rvalue_from_python_stage1_data* data)
    {
        const bp::list &board = boost::python::extract<bp::list>(obj_ptr);

        // Grab pointer to memory into which to construct the new vector<string>
        vector<string>* new_board = (vector<string>*)(
            ((boost::python::converter::rvalue_from_python_storage<vector<string>>*)data)->storage.bytes);

        // in-place construct the new vector<string> using the data
        // extraced from the python object
        new (new_board) vector<string>();

        for (int i = 0; i < len(board); ++i) {
            new_board->push_back(boost::python::extract<string>(board[i]));
        }

        // Stash the memory chunk pointer for later use by boost.python
        data->convertible = new_board;
    }
};

// Struct embedding the vector< vector< pair<uint, uint>>> to python list conversion
struct MoveVectorToPython
{
    MoveVectorToPython()
    {
        bp::to_python_converter<vector<Checkers::Move>, MoveVectorToPython>();
    }

    static PyObject* convert(const vector<Checkers::Move>& moves)
    {
        bp::list list;
        for (const auto &move : moves)
        {
            list.append(move);
        }
        // manually increment python ref counter
        return bp::incref(list.ptr());
    }
};

struct MoveToPython
{
    MoveToPython()
    {
        bp::to_python_converter<Checkers::Move, MoveToPython>();
    }

    static PyObject* convert(const Checkers::Move& moves)
    {
        bp::list list;
        for (auto move : moves)
        {
            list.append(move);
        }
        // manually increment python ref counter
        return bp::incref(list.ptr());
    }
};

struct PositionToPython
{
    PositionToPython()
    {
        bp::to_python_converter<Checkers::Position, PositionToPython>();
    }

    static PyObject* convert(const Checkers::Position& p)
    {
        bp::list list;
        list.append(p.first);
        list.append(p.second);
        // manually increment python ref counter
        return bp::incref(list.ptr());
    }
};



BOOST_PYTHON_MODULE(ai_cpp)
{
    //register converter
    BoardToCpp();
    MoveVectorToPython();
    MoveToPython();
    PositionToPython();

    // enable threads
    PyEval_InitThreads();

    // define python binding entry point
    bp::def("allowed_moves", Checkers::allowedMoves, (bp::arg("board"), bp::arg("color")));
    bp::def("play", Checkers::play, (bp::arg("board"), bp::arg("color")));
}


