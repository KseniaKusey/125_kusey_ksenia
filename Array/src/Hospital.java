import java.util.Random;


public class Hospital {

    public static float[] generatePatientsTemperatures(int patientsCount) {
        if (patientsCount <= 0) {
            return new float[0];
        }
        Random rnd = new Random();
        float min = 32.0f;
        float max = 40.0f;
        float[] temps = new float[patientsCount];
        for (int i = 0; i < patientsCount; i++) {
            float value = min + rnd.nextFloat() * (max - min);
            value = Math.round(value * 10f) / 10f;
            temps[i] = value;
        }
        return temps;

    }

    public static String getReport(float[] temperatureData) {
        /*
        TODO: Напишите код, который выводит среднюю температуру по больнице,количество здоровых пациентов,
            а также температуры всех пациентов.
            Округлите среднюю температуру с помощью Math.round до 2 знаков после запятой,
            а температуры каждого пациента до 1 знака после запятой
        */

        StringBuilder report = new StringBuilder();
        report.append("Температуры пациентов: ");

        float sum = 0;
        int healthyCount = 0;
        for (float temp : temperatureData) {
            report.append(String.format("%.1f ", temp));
            sum += temp;

            if (temp >= 36.2f && temp <= 36.9f) {
                healthyCount++;
            }
        }

        float avg = sum /temperatureData.length;

        report.append("\nСредняя температура: ");
        report.append(String.format("%.2f",avg));
        report.append("\nКоличество здоровых: ");
        report.append(healthyCount);

        return report.toString();



    }
}