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

std::string get_one_logfile(boost::filesystem::path logfile) {
    const char * fname = logfile.c_str();
    printf("Reading %s...\n", fname);
    std::ifstream fh(logfile, std::ios::binary | std::ios::ate);
    const size_t sz = fh.tellg();
    if (sz < 0) {
        printf("File size of %s is less than 0, skipping...",fname);
    }
    fh.seekg(0, std::ios::beg);
    std::string str = std::string(sz, '\0');
    if (fh.is_open())
        fh.read(&str[0],sz);
    fh.close();
    return str;
}

int aggregate_logfiles() {
    path p (LOGDIR);
    try {
        if (exists(p)) {
            int total;
            for (directory_entry& x : directory_iterator(p))
                total += x.path().size();

            std::string buf;
            for (directory_entry& x : directory_iterator(p)) {
                buf.append(get_one_logfile(x.path()));
            }
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
}