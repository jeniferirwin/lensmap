#include "view.cpp"
#include "config.cpp"

class World {
    public:
        static const int WORLD_ROWS = 1300;
        static const int WORLD_COLS = 2000;
        View views[WORLD_ROWS * WORLD_COLS / VIEW_LINES];
        char map[WORLD_ROWS][WORLD_COLS] = {};

    void fill_with_oceans() {
        for (int i = 0; i < WORLD_ROWS; i++) {
            for (int j = 0; j < WORLD_COLS; j++) {
                map[i][j] = 'o';
            }
        }
    }

    void initialize_views() {
        
    }

    void plot_to_array(std::string log) {
        std::size_t view_start = 0;
        while (view_start < log.size()) {
            std::size_t view_end = log.find("[COORDINATES",view_start);
            text_to_view(log, view_start, view_end);
            view_start = view_end;
        }
    }

    void text_to_view(std::string log, std::size_t view_start, std::size_t view_end) {
    }
};