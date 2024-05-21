#ifndef WORLD_H
#define WORLD_H

#include <string>
#include "view.h"
#include "const.h"

class World {
    public:
        char map[WORLD_ROWS][WORLD_COLS] = {};
        View views[WORLD_ROWS * WORLD_COLS / VIEW_LINES];
        void fill_with_oceans();
        void initialize_views();
        void plot_to_array(std::string log);
        void text_to_view(std::string log, std::size_t view_start, std::size_t view_end);
};

#endif