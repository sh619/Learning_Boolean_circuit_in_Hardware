`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/01/03 22:04:52
// Design Name: 
// Module Name: pseudo_linear
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


module pseudo_linear(
    input clk,
    input rstn,
    input [783:0] x, //input mnist image
    input y,//real value
    output reg result
    );
    reg [783:0] p; //parameter value
    reg [783:0] up_p;
    reg [783:0] vec; //Result of the multiplication of parameter and the input
    reg [9:0] num;//the number of "1"s in the bit vector
    reg [9:0] num_p; // the number of "1"s in parameter
    integer i; // loop variable
    integer j;
    integer q;
    //forward model
    always @(posedge clk or negedge rstn) begin
        if(!rstn) begin
            result<=0;
            up_p <=0;
            p<=0;
            vec<=0;
            num<=0;
            num_p<=0;
        end 
        else begin
            for (i =0; i<784;i=i+1 ) begin
                vec[i] <= x[i] & p [i];
            end
            // if it has less than 25% "1"s, it will return 1.
            if(num > (num_p<<2) ) begin
                result <= 0;
            end
            else result <= 1;
        end
    end
    always @(vec or p) begin //Calculate the number of "1"s in the bitvec
        num = 0;
        num_p=0;
        for (q=0; q<784 ;q=q+1) begin
                num = num + vec[q];
                num_p = num_p + p[q];
        end
    end
                
    //Reverse model and update parameters
    always @(posedge clk or negedge rstn) begin
        if(!rstn) begin
            result<=0;
            up_p <=0;
            p<=0;
            vec<=0;
            num<=0;
            num_p<=0;
        end 
        else begin
        if(result != y) begin
            for (j =0; j<784;j=j+1) begin
                up_p[j] <= x[j] ^ p[j];
            end
        end
        p <= up_p;
        end
    end
endmodule
