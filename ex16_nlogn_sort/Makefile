CC=	gcc
CFLAGS=	-Wall -std=gnu99 -g
LD=	gcc
LDFLAGS=

all: time_sorts

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $^

time_sorts:	time_sorts.o merge_sort.o quicksort.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f time_sorts *.o