package org.Base;

import WebHandler.ServerSide;
import TerminalHandler.SocketSide;
import java.net.*;
import java.io.*;

public class ServerBootup {
	public static void starter(int Port) throws IOException {
		 int httpPort;
		 int socketPort;

		if (Port != 0){
			 httpPort = Port;
			 socketPort = Port + 1010;
		} else {
			httpPort = 8080;
			socketPort = httpPort + 1010;
		}
		//Starts Both Servers on separate Threads
		new Thread(() -> ServerSide.startServerWeb(httpPort)).start();
		new Thread(() -> SocketSide.startServerSocket(socketPort)).start();

		//Feedback to System
		System.out.println("HTTP Server started on Port: " + httpPort);
		System.out.println("Socket Server started on Port: " + socketPort);

	}
}
