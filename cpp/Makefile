OBJDIR = obj

# Specify the compiler to use
CC = g++

# Specify the compiler flags
CFLAGS = -Wall -Wextra -std=c++11

# Specify the source files
SRCS = $(wildcard *.cpp)

# Specify the executable name
TARGET = lensmap

# Specify the target that should be built by default
all: $(TARGET)

# Compile the source files into object files
$(OBJDIR)/%.o: %.cpp
	$(CC) -c $(CFLAGS) $< -o $@

# Link the object files into the executable
$(TARGET): $(patsubst %.cpp,$(OBJDIR)/%.o,$(SRCS))
	$(CC) $(CFLAGS) $^ -o $@ -lboost_filesystem

# Clean up the object files
clean:
	rm -f $(OBJDIR) $(TARGET)