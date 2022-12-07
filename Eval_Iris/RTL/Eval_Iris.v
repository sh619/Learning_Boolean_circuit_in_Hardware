`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2022/11/29 14:32:28
// Design Name: 
// Module Name: Eval_Iris
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////

module Eval_Iris(
    input clk,
    input [3:0] x,
    input y,
    input rst_n,
    output [15:0] p,
    output wire prediction
    );
    reg [15:0] rdiff;
    reg  [15:0] curr_p;
    reg [15:0] up_d=16'h0;
    //forward eval model
    assign prediction = curr_p[x];

    //Calculate reverse derivative
    always @(*) begin
     begin
        rdiff =0;
        if (prediction != y)begin
            rdiff =(16'b1 << x);
        end
        else begin
            rdiff = 16'h0;
        end
        up_d  =  rdiff ^ curr_p;
        end
    end 

    // Update parameters
    always @(posedge clk or negedge rst_n ) begin
        if (!rst_n) begin
            curr_p <=16'b0000000000000000;
            end
        else begin
            curr_p <= up_d;
        end
    end
    // Output current parameter
    assign p =curr_p;

endmodule
