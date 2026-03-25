import { Client_InterfaceClient } from "@/proto/Client_interfaceServiceClientPb";

const GRPC_URL = import.meta.env.VITE_GRPC_URL ?? "http://localhost:8080";
export const parkingClient = new Client_InterfaceClient(GRPC_URL);
