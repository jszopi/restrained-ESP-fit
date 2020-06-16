
# Fortran compiler: gfortran, g77, ifort, pgf77...
FC = gfortran

FLAGS = -c -O2
# -mcmodel=medium
# option for gfortran
# allows handling of a larger number of MEP on 64 bit system
# FLAGS = -c -mcmodel=medium -O2

OBJS= resp.o
SRCS= resp.f
LIB= shared_variables.h


ifeq ($(shell uname -s),Linux)
	VPATH_DIR = /usr/lib/gcc/x86_64-linux-gnu/9
else
	VPATH_DIR = /usr/local/Cellar/gcc/9.3.0_1/lib/gcc/9
	FLAGS += -dynamiclib
endif

vpath %.a $(VPATH_DIR)

STATICLIBS = -lgfortran -lquadmath
.LIBPATTERNS = lib%.a lib%.dylib lib%.so

resp:	$(OBJS) $(STATICLIBS)
	# Based on: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=46539#c3
	# and https://stackoverflow.com/a/5583245
	$(FC) $^ -lm -o resp

$(OBJS): $(SRCS) $(LIB)
	$(FC) $(FLAGS) $(SRCS)

clean:
	rm -rf $(OBJS) resp

