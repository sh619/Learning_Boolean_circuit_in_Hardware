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


module pseudo_linear_0(
    input clk,
    input rst_n,
    input [3:0] threshold,
    input [793:0] image_data,
    output y,
    output reg result,
    output [783:0] pm
    );
    reg  [784:1] p ; //parameter
    reg  [784:0] data_in;
    reg  [783:0] bitvec;//resulting bitvec
    reg  [784:1] re_d;//The reverse derivitive of the function
    reg error; // The error between the output and the prediction
    reg [9:0] num_p;
    reg [9:0] num;
    reg [9:0] num_r;
    reg [9:0] num_p_r;
    integer i,j,m,n,q,s; // loop variable
    initial begin
        p=0;
        bitvec=0;
        re_d=0;
        num_p=0;
        num=0;
        num_p_r=0;
        num_r=0;
        error =0;
    end

    // //Connect the Random number generator
    // LFSR RNG (
    //     .clk(clk),
    //     .rst_n(rst_n),
    //     .Q(train_num)
    // );

    always @(*) begin
        bitvec = p & image_data[793:10];
        num=0;
        num_p=0;
            for (j =0; j <784 ; j=j+1) begin //Calculate the number of "1"s in the resulting bitvec   
                num=bitvec[j] ? num+1 : num;
            end 
            for (i = 1; i<785 ; i=i+1) begin //Calculate the number of "1"s in the parameter
                num_p= p[i] ? num_p+1 : num_p;
            end  
        result = forward(num,num_p);
        error = result ^ image_data[0];
        if(error) begin
        for (m=0; m<784;m=m+1) begin
                num_r =(image_data[m+10]) ? ((p[m]) ? (num-1) : (num+1) ) : num;
                num_p_r = (p[m]) ? (num_p - 1) : (num_p+1);    
                re_d[m] = result ^ forward(num_r,num_p_r);
            end
        end
        else begin
            re_d=0;
        end
    end

    always @(posedge clk or negedge rst_n) begin
        if(!rst_n) begin
        p<=0;
        end
        else begin
            p <= p ^re_d;
        end
    end
    // Reverse model
    // always @(*) begin
    //     if(error) begin
    //     for (m=0; m<784;m=m+1) begin
    //             num_r =(image_data[m]) ? ((p[m]) ? num-1 : num+1 ) : num;
    //             num_p_r = (!p[m]) ? num_p + 1 : num_p-1;
    //             re_d[m] = result ^ forward(num_r,num_p_r);
    //         end
    //     end
    //     else begin
    //         re_d<=0;
    //     end

    // end

    assign y=image_data[0];
    //Output the parameter value
    assign pm=p;
        //forward model
    function forward;
        input [9:0] num_r;
        input [9:0] num_p_r;
        begin
            if(((num_p_r >> threshold))>= num_r) //Threshold value
            begin
                forward = 1'b0;            
            end
            else begin
                forward = 1;   
            end
        end    
    endfunction
endmodule