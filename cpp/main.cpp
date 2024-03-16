#include <iostream>
#include <fstream>
#include <stdio.h>
#include <dirent.h>
#include <string.h>
#include <boost/filesystem.hpp>
using namespace boost::filesystem;

const int WORLD_ROWS = 1300;
const int WORLD_COLS = 2000;
const std::string LOGDIR = "../logfiles/";

char map[WORLD_ROWS][WORLD_COLS] = {};

int get_one_logfile(boost::filesystem::path file) {
    printf("%s\n", file.filename().c_str());
    return 0;
}

int aggregate_logfiles() {
    path p (LOGDIR);
    try {
        if (exists(p)) {
            for (directory_entry& x : directory_iterator(p))
                get_one_logfile(x.path());
        }
    }
    
    catch (const filesystem_error& err) {
        std::cout << err.what() << '\n';
    }

    return 0;
}

void fill_with_oceans() {
    for (int i = 0; i < WORLD_ROWS; i++) {
        for (int j = 0; j < WORLD_COLS; j++) {
            map[i][j] = 'o';
        }
    }
}

int main() {
    aggregate_logfiles();
    fill_with_oceans();
    printf("%c",map[200][3]);
}