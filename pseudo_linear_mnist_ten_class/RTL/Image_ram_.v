`timescale 1ns / 1ps
// Single-Port Block RAM Write-First Mode
module Image_RAM_train
#(
    parameter ADDR_WIDTH = 16,
    parameter DATA_WIDTH = 794,
    parameter DEPTH = 60000
)
(clk, we, en, addr, data_in, dout);
input clk; 
input we;
input en;
input [ADDR_WIDTH-1:0] addr;
input [DATA_WIDTH-1:0] data_in; 
output [DATA_WIDTH-1:0] dout;
(* ram_style = "ultra" *) reg [DATA_WIDTH-1:0] RAM [DEPTH-1:0];
reg [DATA_WIDTH-1:0] dout;

initial begin
    $readmemb("final_train.mem", RAM);
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