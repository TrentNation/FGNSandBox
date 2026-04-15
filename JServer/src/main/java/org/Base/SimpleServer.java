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
		}
	}
	static void handleClient(Socket socket) {
		try{
				BufferedReader in = new BufferedReader(
						new InputStreamReader(socket.getInputStream()));
				PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
				String message = in.readLine();
				while (message != null) {
					System.out.println("Received: " + message);
					out.println("Echo: "+ message);
				}

			} catch(IOException io) {
			io.printStackTrace();
		}
	}

}
