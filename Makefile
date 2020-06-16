
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

resp:	$(OBJS) 
	# Based on: https://gcc.gnu.org/bugzilla/show_bug.cgi?id=46539#c3
	$(FC) $(OBJS) -Wl,-Bstatic -lgfortran -lquadmath -Wl,-Bdynamic -o resp

$(OBJS): $(SRCS) $(LIB)
	$(FC) $(FLAGS) $(SRCS)

clean:
	rm -rf $(OBJS) resp

