import java.util.Arrays;

class Ideone {
    public static void main(String[] args) {
        // Test case
        int physics = 90;
        int chemistry = 87;
        int mathematics = 95;
        int englishLanguage = 80;
        int hindiLanguage = -1; // Marked as -1 for excluded subjects
        int sanskrit = 85;
        int supw = -1; // Marked as -1 for excluded subjects
        int hindiLiterature = -1;
        int englishLiterature = 82;
        int elective1 = 88;
        int elective2 = -1; // Marked as -1 for excluded subjects
        int elective3 = -1;

        double percentage = calculatePercentage(physics, chemistry, mathematics, englishLanguage, hindiLanguage, sanskrit, supw, hindiLiterature, englishLiterature, elective1, elective2, elective3);
        System.out.println("Best of Five Percentage: " + percentage);
    }

    public static double calculatePercentage(int physics, int chemistry, int mathematics, int englishLanguage, int hindiLanguage, int sanskrit, int supw, int hindiLiterature, int englishLiterature, int elective1, int elective2, int elective3) {
        int[] marksArray = new int[10]; // Total of 10 subjects (including mandatory PCM)
      
        marksArray[0] = englishLanguage;
        marksArray[1] = hindiLanguage;
        marksArray[2] = sanskrit;
        marksArray[3] = supw;
        marksArray[4] = hindiLiterature;
        marksArray[5] = englishLiterature;
        marksArray[6] = elective1;

        // Sort the marks array in descending order
        Arrays.sort(marksArray);
        int sum = physics+chemistry+mathematics ;
        int count = 3;

        // Iterate over the sorted marks array and calculate the sum of the best five subjects
        for (int i = marksArray.length - 1; i >= 0; i--) {
            if (marksArray[i] != -1) {
                sum += marksArray[i];
                count++;
            }
            if (count == 5 && marksArray[i] < marksArray[i+1]) {
                break;
            }
            if (count == 7){
            	break;
            }
        }

        // Calculate the percentage
        double percentage = (sum / 500.0) * 100;

        return percentage;
    }
}