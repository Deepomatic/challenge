#pragma once

#include <vector>
#include <string>

namespace checkers{

class Checkers
{
public:
    // 2d coordinates
    using Position = std::pair<uint8_t, uint8_t>;

    // move representation
    using Move = std::vector<Position>;

    // alowed_moves :
    //  c++ implementation of the ai.allowed_moves python method
    static std::vector<Checkers::Move> allowedMoves(const std::vector<std::string> &board, const std::string &color);

    // play :
    //  c++ implementation of the ai.play python method
    static Checkers::Move play(const std::vector<std::string> &board, const std::string &color);
};


} // checkers
