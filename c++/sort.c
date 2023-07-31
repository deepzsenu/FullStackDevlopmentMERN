#include <stdio.h>
#include <stdlib.h>

int main() {
  // Initialize variables
  int i, j, n;
  float id[15];
  float average;

  // Open input file
  FILE *inputFile = fopen("Input_file.txt", "r");
  if (inputFile == NULL) {
    printf("Error opening input file.\n");
    return 1;
  }

  // Read values from input file
  for (i = 0; i < 15; i++) {
    fscanf(inputFile, "%f", &id[i]);
  }

  // Close input file
  fclose(inputFile);

  // Sort the values in the array
  for (i = 0; i < 14; i++) {
    for (j = i + 1; j < 15; j++) {
      if (id[i] > id[j]) {
        float temp = id[i];
        id[i] = id[j];
        id[j] = temp;
      }
    }
  }

  // Calculate the average
  average = 0;
  for (i = 0; i < 15; i++) {
    average += id[i];
  }
  average /= 15;

  // Open output file
  FILE *outputFile = fopen("Output_file.txt", "w");
  if (outputFile == NULL) {
    printf("Error opening output file.\n");
    return 1;
  }

  // Print the sorted values to the output file
  fprintf(outputFile, "ID sorted result: ");
  for (i = 0; i < 15; i++) {
    fprintf(outputFile, "%.1f ", id[i]);
  }

  // Print the average to the output file
  fprintf(outputFile, "\nThe average = %.1f\n", average);

  // Close output file
  fclose(outputFile);

  return 0;
}
