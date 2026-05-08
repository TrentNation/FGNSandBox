package WebHandler;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Path;

public class ServerSide {



	/**
	 * Purpose: Handles The Server Function for Web Pages.
	 * @param PORT : Holds the Main Server Port Number
	 */
	public static void startServerWeb(int PORT){
		try(ServerSocket server = new ServerSocket(PORT)){
			System.out.println("Web Server STARTED");
			while (true){
				Socket webClient = server.accept();
				new Thread(() -> handleClientWebPage(webClient)).start();
			}
		}catch (IOException io){
			System.out.println("Web Server ERROR: " + io.getMessage());
		}
	}
	/**
	 * Purpose: The WebPage Section
	 * Future Plans: Opens an HTML file for the User
	 * @param socket
	 */
	static void handleClientWebPage(Socket socket) {
		try(BufferedReader in = new BufferedReader(
				new InputStreamReader(socket.getInputStream()));
		    PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
		){
			System.out.println("Are...we...connected? " + socket.getInetAddress());

			String line = in.readLine(); //To read the Header & Check the file

			while(!(in.readLine()).isEmpty()){
				out.println(line); //FIller for now
			}
			if (line == null) return;
			String path = line.split(" ")[1];

			//If root was requested
			if (path.equals("/")) path = "/index.html";
			Path filePath = Path.of("resources" + path);
			if (Files.exists(filePath)) {
				//Sends an HTTP Response
				String body = Files.readString(filePath);
				out.println("HTTP/1.1 200 OK");
				out.println("Content-Type: text/html");
				out.println("Content-Length: " + body.length());
				out.println(body);
			}
			else {
				String body = "<html> <body><h1> 404 File Not Found </h1></body></html";
				out.println("HTTP/1.1 404 Not Found");
				out.println("Content-Type: text/html");
				out.print(body);
			}
		} catch (IOException io) {
			System.out.println("Client ERROR: " + io.getMessage());
		}
	}

	static void uploadWebPage(){
		System.out.println("Uploading Web Page.");
	}
}
