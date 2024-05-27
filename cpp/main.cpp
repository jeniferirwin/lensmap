#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <boost/filesystem.hpp>
#include "logfiles.h"
#include "world.h"

int main(void) {
    std::cout << "Hello, World!\n" << std::endl;
    const char * log = "";
    if (log == "") { return 1; }
    World world = World();
    world.fill_with_oceans();
    world.initialize_views();
    world.plot_to_array(log);
}