#include <iostream>
#include <fstream>
#include <stdio.h>
#include <dirent.h>
using namespace std;

const int WORLD_ROWS = 1300;
const int WORLD_COLS = 2000;
const char * LOGDIR = "../logfiles/";
char map[WORLD_ROWS][WORLD_COLS] = {};

int get_logfiles() {
    struct dirent *entry = nullptr;
    DIR *dp = nullptr;
    dp = opendir(LOGDIR);
    if (dp != nullptr) {
        while ((entry = readdir(dp)))
            printf("%s\n", entry->d_name);
    }
    closedir(dp);
    return 0;
}

int fill_with_oceans() {
    for (int i = 0; i < WORLD_ROWS; i++) {
        for (int j = 0; j < WORLD_COLS; j++) {
            map[i][j] = 'o';
        }
    }
}

int main() {
    ofstream myfile;
    myfile.open("example.txt");
    myfile << "Writing this to a file.\n";
    myfile.close();
    
    get_logfiles();
    fill_with_oceans();
    printf("%c",map[200][3]);
}