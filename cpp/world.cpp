#include "const.h"
#include "world.h"

void World::fill_with_oceans() {
    for (int i = 0; i < WORLD_ROWS; i++) {
        for (int j = 0; j < WORLD_COLS; j++) {
            map[i][j] = 'o';
        }
    }
}

void World::initialize_views() {
    
}

void World::plot_to_array(std::string log) {
    std::size_t view_start = 0;
    while (view_start < log.size()) {
        std::size_t view_end = log.find("[COORDINATES",view_start);
        text_to_view(log, view_start, view_end);
        view_start = view_end;
    }
}

void World::text_to_view(std::string log, std::size_t view_start, std::size_t view_end) {

}
