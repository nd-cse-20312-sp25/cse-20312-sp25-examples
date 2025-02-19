CC= gcc
CFLAGS= -Wall -g -std=gnu99
LD= gcc
LDFLAGS=
TARGETS= hash_table_demo

all: $(TARGETS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

hash_table_demo: pair.o hash.o table.o hash_table_demo.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f hash_table_demo *.o
