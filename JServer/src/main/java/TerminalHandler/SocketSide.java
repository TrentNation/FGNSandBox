package TerminalHandler;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class SocketSide {
	/**
	 * Purpose: Handles The Server Function for Raw Sockets
	 * @param PORT
	 */
	public static void startServerSocket(int PORT){
		try(ServerSocket server = new ServerSocket(PORT);)
		{
			System.out.println("Socket Server STARTED");
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



}
