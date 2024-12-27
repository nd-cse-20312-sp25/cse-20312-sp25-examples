score:
	@$(MAKE) -sk score_all

score_all: score_unit_duplicates

score_unit_duplicates: unit_duplicates
	./score_unit_duplicates.sh

all: unit_duplicates time_duplicates

#--------- Do not modify above this line -----------------

duplicates.o: duplicates.c duplicates.h
	gcc -Wall -g -c duplicates.c

unit_duplicates.o: unit_duplicates.c duplicates.h
	gcc -Wall -g -c unit_duplicates.c

unit_duplicates: duplicates.o unit_duplicates.o
	gcc -o unit_duplicates duplicates.o unit_duplicates.o

time_duplicates.o: time_duplicates.c duplicates.h
	gcc -Wall -g -c time_duplicates.c

time_duplicates: duplicates.o time_duplicates.o
	gcc -o time_duplicates duplicates.o time_duplicates.o

clean:
	rm *.o unit_duplicates time_duplicates