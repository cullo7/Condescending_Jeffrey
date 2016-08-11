#include <stdio.h>
#include <string.h>

/*
 * Short script to take quotes out of csv files in order for the to be parsed
 * in the future.
 */

int main()
{
   int mychar = 0;
   FILE *ifile;
   FILE *ofile;
  char* in = "country_mapping.txt"; 
  char* out = "country_mapping_no_quotes.txt";

   ifile = fopen(in, "r");
   ofile = fopen(out, "w");
   if(ifile == NULL)
   {
     printf("Error opening %s for writing. Program terminated.", in);
   }
	if(ofile == NULL)
   {
     printf("Error opening %s for reading. Program terminated.", out);
   }

	while((mychar = fgetc(ifile)) != EOF){
    if(mychar != (int)'"'){
      fputc(mychar, ofile);
    }
	}

  fclose(ifile);
  fclose(ofile);
  return 0;
}

