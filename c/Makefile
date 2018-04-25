CC = gcc
CFLAGS = -c
#LFLAGS = 

OBJS = cc6809.o file_lib.o

%.o: %.c
	$(CC) $(CFLAGS) $<

cc6809: $(OBJS)
	$(CC) -o $@ $(OBJS)

clean:
	rm -f $(OBJS)
	rm -f cc6809
