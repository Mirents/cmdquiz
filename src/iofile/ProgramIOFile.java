package iofile;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.BufferedReader;
import java.io.FileReader;

public class ProgramIOFile {

	public static void main(String[] args) {
		// Работа с файлом происходит в	нутри обработчика исключений
		// Создание объекта для чтения данных из файла
		BufferedReader br = null;
		try {
			// Создание переменной файла для работы с ним
			File iofile = new File("iofile.txt");
			// Проверка наличия файла на диске и создание его в случае отсутствия
			if(iofile.exists())
				{
					iofile.createNewFile();
				}
			// Создание объекта для записи данных в файл
			PrintWriter pw = new PrintWriter(iofile);
			// Запись данных в файл
			pw.println("I am is study!");
			pw.println("Das ist fantastisch	!");
			pw.println("Hello Darya!");
			// Закрытие файла после использвания
			pw.close();
			// Определение объекта для чтения файла
			br = new BufferedReader(new FileReader("iofile.txt"));
			// Переменная для считывания данных из файла
			String line;
			// Процесс считывания из файла
			while((line = br.readLine()) != null)
			{
				System.out.println(line);
			}
		} catch(IOException e) {
			System.out.print("Error " + e);
		}
		finally
		{
			try
			{
				br.close();
			} catch(IOException e)
			{
				System.out.print("Error " + e);
			}
		}

	}

}
