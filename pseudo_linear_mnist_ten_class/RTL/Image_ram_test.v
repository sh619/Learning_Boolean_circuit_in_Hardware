`timescale 1ns / 1ps
// Single-Port Block RAM Write-First Mode
module Image_RAM_test
#(
    parameter ADDR_WIDTH = 11,
    parameter DATA_WIDTH = 784,
    parameter DEPTH = 2048
)
(clk, we, en, addr, data_in, dout);
input clk; 
input we;
input en;
input [ADDR_WIDTH-1:0] addr;
input [DATA_WIDTH-1:0] data_in; 
output [DATA_WIDTH-1:0] dout;
(* ram_style = "block" *) reg [DATA_WIDTH-1:0] RAM [DEPTH-1:0];
reg [DATA_WIDTH-1:0] dout;

initial begin
    $readmemb("final_test.mem", RAM);
end

always @(posedge clk)
begin
 if (en)
 begin
 if (we)
 begin
    RAM[addr] <= data_in;
 end
 else
 dout <= RAM[addr];
end
end
endmodule