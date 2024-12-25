CC=	gcc
CFLAGS=	-Wall -g -std=gnu99
LD=	gcc
LDFLAGS=
TARGETS= unit_stack unit_array pbb_matched

all: $(TARGETS)

%.o: %.c
	$(CC) $(CFLAGS) -c -o $@ $<

unit_array: unit_array.o array.o
	$(LD) $(LDFLAGS) -o $@ $^

unit_stack: unit_stack.o stack.o array.o
	$(LD) $(LDFLAGS) -o $@ $^

pbb_matched: pbb_matched.o stack.o array.o
	$(LD) $(LDFLAGS) -o $@ $^

clean:
	rm -f $(TARGETS) *.o
