package homework12.no2;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class ConfigReader {
    public static void main(String[] args) throws IOException {
        Properties properties = new Properties();
        try (FileInputStream input = new FileInputStream("myInfo.config")) {
            properties.load(input);
        }

        String stuId = properties.getProperty("stuID");
        String stuName = properties.getProperty("stuName");

        System.out.println("学号: " + stuId);
        System.out.println("姓名: " + stuName);
    }
}
