#include <iostream>
#include <boost/filesystem.hpp>
#include "logfiles.h"
#include "const.h"
using namespace boost::filesystem;


std::string aggregate_logfiles() {
    path p (LOGDIR);
    if (exists(p)) {
        int total;
        for (directory_entry& x : directory_iterator(p))
            total += x.path().size();

        std::string buf;
        for (directory_entry& x : directory_iterator(p)) {
            buf.append(get_one_logfile(x.path()));
        }
        printf("Read in %lu bytes (%lu KB, %lu MB)\n",buf.size(), buf.size() / 1024, buf.size() / 1024 / 1024);
        return buf;
    }
    return "";
}

std::string get_one_logfile(path logfile) {
    const char * fname = logfile.c_str();
    printf("Reading %s...\n", fname);
    std::ifstream fh(fname, std::ios::binary | std::ios::ate);
    const size_t sz = fh.tellg();
    if (sz <= 0) {
        printf("File size of %s is less than 0, skipping...",fname);
        return "";
    }
    fh.seekg(0, std::ios::beg);
    std::string str = std::string(sz, '\0');
    fh.read(&str[0], sz);
    return str;
}
