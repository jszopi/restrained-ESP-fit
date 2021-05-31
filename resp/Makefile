
# Fortran compiler: gfortran, g77, ifort, pgf77...
FC = $(or $(RESP_COMPILER),gfortran)

FLAGS = -c -O2
# -mcmodel=medium
# option for gfortran
# allows handling of a larger number of MEP on 64 bit system
# FLAGS = -c -mcmodel=medium -O2

OBJS= resp.o  
SRCS= resp.f
LIB= shared_variables.h

resp:	$(OBJS) 
	$(FC) $(OBJS) -o resp

$(OBJS): $(SRCS) $(LIB)
	$(FC) $(FLAGS) $(SRCS)

clean:
	rm -rf $(OBJS) resp

