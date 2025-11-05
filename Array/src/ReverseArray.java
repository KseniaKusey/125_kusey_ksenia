public class ReverseArray {


    public static String[] reverse(String[] strings) {
        //TODO: Напишите код, который меняет порядок расположения элементов внутри массива на обратный.
        for(int i = 0 , j = strings.length - 1; i < j; i++, j--) {
            String words = strings[i];
            strings[i] = strings[j];
            strings[j] = words;
        }
        return strings;
    }

}
