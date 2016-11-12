use_cpp_implementation = False

import sys
if use_cpp_implementation:
    sys.path.append("cpp/build/")
    import ai_cpp as ai
else:
    import ai
