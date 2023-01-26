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
    input rst_n,
    input [13:0] x, //input address of the mnist image
    input y,//real value
    output reg result
    );
    reg  [783:0] p ; //parameter
    reg  [783:0] data_in;
    reg  [783:0] up_p; //Updated parameter
    reg  [783:0] bitvec;//resulting bitvec
    reg  [783:0] re_d;//The reverse derivitive of the function
    wire [783:0] image_data; //output from the image RAM
    reg [9:0] num_p;
    reg [9:0] num;
    reg [9:0] num_r;
    reg [9:0] num_p_r;
    wire we; // image RAM write enable
    wire en; // image RAM enable
    reg done;
    integer i,j,m,n,q,s; // loop variable

    assign en =1;
    assign we =0;
    initial begin
        p=0;
        up_p=0;
        bitvec=0;
        re_d=0;
        num_p=0;
        num=0;
    end
    //Connect the image RAM
    Image_RAM Image_data (
        .clk(clk),
        .we(we),
        .en(en),
        .addr(x),
        .dout(image_data),
        .data_in(data_in)
    );

    always @(image_data) begin
        bitvec = p & image_data;
        num=0;
            for (j =0; j <784 ; j=j+1) begin //Calculate the number of "1"s in the resulting bitvec   
                num=bitvec[j] ? num+1 : num;
            end 
        num_r = num;
        num_p=0;
        for (i = 0; i<784 ; i=i+1) begin //Calculate the number of "1"s in the parameter
                num_p= p[i] ? num_p+1 : num_p;
            end
        num_p_r = num_p;    
        result = forward(num,num_p);
    end
    

    // Reverse model
    always @(*) begin
        if(result != y ) begin
        for (m=0; m<784;m=m+1) begin
                num_r=(image_data[m]) ? ((p[m]) ? num_r-1 : num_r+1 ) : num_r;
                num_p_r = (!p[m]) ? num_p_r + 1 : num_p_r-1;
                re_d [m] = result ^ forward(num_r,num_p_r);
                num_r=num;
                num_p_r = num_p;
            end
        p=p^re_d;
        end
        else begin
            num_p_r=num_p;
            num_r = num_r;
            re_d=0;
        end

    end

        //forward model
    function forward;
        input [9:0] num;
        input [9:0] num_p;
        begin
            if((num_p >> 2) >= num) //Threshold value
            begin
                forward = 1;            
            end
            else begin
                forward = 0;   
            end

        end    
    endfunction
endmodule