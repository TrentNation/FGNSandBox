package org.Base;

import java.net.*;
import java.io.*;
import java.util.Scanner;

public class SimpleServer {
	public static void main(String[] args) throws IOException {
		final int PORT = 8080;
		ServerSocket serverSocket = new ServerSocket(PORT);
		System.out.println("SERVER STARTED\nPort:" + PORT);
		while (true) {
			//Block and Wait for a client to connect
			Socket clientSocket = serverSocket.accept();
			System.out.println("Client CONNECTED" + clientSocket.getInetAddress());

			//Handle the Client in a new thread(Allowing us to serve multiple clients)
			new Thread(() -> handleClient(clientSocket)).start();
			new Thread(() -> handleClientWebPage(clientSocket)).start();
		}
	}

	static void handleClient(Socket socket) {
		try {
			BufferedReader in = new BufferedReader(
					new InputStreamReader(socket.getInputStream()));
			PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
			String message;
			while ((message = in.readLine()) != null) {
				System.out.println("Received: " + message);
				out.println("Echo:  " + message);
			}

		} catch (IOException io) {
			io.printStackTrace();
		}
	}

	//For the purpose of Handling WebPage Responses
	static void handleClientWebPage(Socket socket) {
		try (
				BufferedReader in = new BufferedReader(
						new InputStreamReader(socket.getInputStream()));
				PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
		) {   //Reading the HTTP request
			String line;
			while (!(line = in.readLine()).isEmpty()) {
				System.out.println("Received: " + line);
			}
			//Send an HTTP response
			String body = "<html><body><h1>We Are Here, Together!</h1></body></html>";
			out.println("HTTP/1.1 200 OK");
			out.println("Content-Type: text/html");
			out.println("Content-Length: " + body.length());
			out.println(body);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	static void uploadWebPage(){
		System.out.println("Uploading Web Page.");
	}
}
