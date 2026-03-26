import { createClient } from "@connectrpc/connect";
import { createGrpcWebTransport } from "@connectrpc/connect-web";
import { Client_Interface } from "@/proto/client_interface_pb.js";

const transport = createGrpcWebTransport({
    baseUrl: import.meta.env.VITE_GRPC_URL ?? "http://localhost:8080",
});

export const parkingClient = createClient(Client_Interface, transport);