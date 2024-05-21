#ifndef LOGFILES_H
#define LOGFILES_H

#include <iostream>
#include <boost/filesystem.hpp>

std::string aggregate_logfiles();
std::string get_one_logfile(boost::filesystem::path logfile);

#endif