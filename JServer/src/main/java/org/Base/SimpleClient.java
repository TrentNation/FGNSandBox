package org.Base;
import java.io.*;
import java.net.*;

public class SimpleClient {
	public static void main(String[] args) throws IOException {
		//The port (should be easily grabbed via elsewhere
		final int PORT = 8080;
		//Connect to the Localhost
		Socket socket = new Socket("localhost",  PORT);

		PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
		BufferedReader in = new BufferedReader(
				new InputStreamReader(socket.getInputStream()));
		//Send a basic Message
		out.println("Hello, Server!");

		String response = in.readLine();
		System.out.println("Server says: " + response);

		socket.close();
	}
}
