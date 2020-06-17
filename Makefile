
# Fortran compiler: gfortran, g77, ifort, pgf77...
FC = gfortran

FLAGS = -c -O2 -v
# -mcmodel=medium
# option for gfortran
# allows handling of a larger number of MEP on 64 bit system
# FLAGS = -c -mcmodel=medium -O2

OBJS= resp.o
SRCS= resp.f
LIB= shared_variables.h

vpath %.a $(VPATH_DIR)

STATICLIBS = -lgfortran -lquadmath
.LIBPATTERNS = lib%.a lib%.dylib lib%.so

resp:	$(OBJS) $(STATICLIBS)
	# Based on: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=46539#c3
	# and https://stackoverflow.com/a/5583245
	$(FC) $^ -o resp

$(OBJS): $(SRCS) $(LIB)
	$(FC) $(FLAGS) $(SRCS)

clean:
	rm -rf $(OBJS) resp

