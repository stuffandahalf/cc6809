CC = gcc
CFLAGS = -c
#LFLAGS = 

OBJS = cc6809.o cc_lib.o file_lib.o string_lib.o

%.o: %.c
	$(CC) $(CFLAGS) $<

cc6809: $(OBJS)
	$(CC) -o $@ $(OBJS)

run: cc6809 ../sample.c
	./cc6809 ../sample.c

clean:
	rm -f $(OBJS)
	rm -f cc6809
