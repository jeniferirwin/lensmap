#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <boost/filesystem.hpp>
#include "view.cpp"
#include "logfiles.cpp"
#include "world.cpp"

int main() {
    std::string log = aggregate_logfiles();
    if (log.empty()) { return 1; }
    World world = World();
    world.fill_with_oceans();
    world.initialize_views();
    world.plot_to_array(log);
}