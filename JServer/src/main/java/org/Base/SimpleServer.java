package org.Base;

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class SimpleServer {
	public static void main(String[] args) throws IOException {
		final int httpPort = 8080;
		final int socketPort = httpPort + 1010;
		//Starts Both Servers on separate Threads
		new Thread(() -> startServerWeb(httpPort)).start();
		new Thread(() -> startServerSocket(socketPort)).start();

		//Feedback to System
		System.out.println("HTTP Server started on Port: " + httpPort);
		System.out.println("Socket Server started on Port: " + socketPort);

	}



	/**
	 * Purpose: Handles The Server Function for Web Pages.
	 * @param PORT : Holds the Main Server Port Number
	 */
	static void startServerWeb(int PORT){
		try(ServerSocket server = new ServerSocket(PORT)){
			System.out.println("SERVER STARTED");
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

		String line;
		while(!(line = in.readLine()).isEmpty()){
			out.println(line);
		}
		//Sends an HTTP Response
		String body = "<html><body><h1>We Are Here, Together!</h1></body></html>";
		out.println("HTTP/1.1 200 OK");
		out.println("Content-Type: text/html");
		out.println("Content-Length: " + body.length());
		out.println(body);
	} catch (IOException io) {
		System.out.println("Client ERROR: " + io.getMessage());
	}
	}

	/**
	 * Purpose: Handles The Server Function for Raw Sockets
	 * @param PORT
	 */
	static void startServerSocket(int PORT){
		 try( ServerSocket server = new ServerSocket(PORT);)
		 {
			 System.out.println("Server STARTED");
			 while (true){
				 Socket clientSocket = server.accept();
				 new Thread (() -> handleClientSocket(clientSocket)).start();
			 }

		 }catch (IOException io){
			 System.out.println("Server ERROR: " + io.getMessage());
		 }
	}

	/**
	 * Purpose: The Socket Function
	 * Future Ideas: Maybe System Details?
	 * @param socket
	 */
	static void handleClientSocket( Socket socket) {
		try(
				BufferedReader in = new BufferedReader(
						new InputStreamReader(socket.getInputStream()));
				PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
				)
				 {


			//Send a Socket response
			String message;
			while ((message = in.readLine()) != null) {
				System.out.println("Received: " + message); //System Message
				out.println("Echo: " + message); //Reponse Message
			}

		} catch (Exception e) {
			System.out.println("Client ERROR: " + e.getMessage());
		}
	}

	static void uploadWebPage(){
		System.out.println("Uploading Web Page.");
	}
}
