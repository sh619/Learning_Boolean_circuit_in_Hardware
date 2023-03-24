`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/02/21 15:49:55
// Design Name: 
// Module Name: mnist_ten
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


module mnist_ten(
    input clk,
    input rst_n,
    input [3:0] threshold,
    output [9:0] train_result,
    output [9:0] test_result
);

// reg [16:0] counter1,counter2,counter3,counter4,counter5,counter6,counter7,counter8,counter9;
integer j;
reg [14:0] train_addr; // train data address
reg [10:0] test_addr; //test data address
wire [783:0] p0,p1,p2,p3,p4,p5,p6,p7,p8,p9;
wire [9:0] label;
wire [783:0] test_image_data;
wire [793:0] train_image_data;
wire we; // image RAM write enable
wire en; // image RAM enable
assign en =1;
assign we =0;

//Connect the RAM that contains the train image
Image_RAM_train Image_train (
    .clk(clk),
    .addr(train_addr),
    .dout(train_image_data),
    .en(en),
    .we(we)
);


//counters for the address in the block RAM
//Address 
always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        train_addr <= 0;
        test_addr <= 0;
    end
    else begin
        if(train_addr == 16'd60000) begin
            train_addr <=0;
            test_addr <= test_addr +1;
        end
        else if (test_addr == 11'd2047) begin
            train_addr <= train_addr +1;
            test_addr <= 0;
        end
        else begin
            train_addr <= train_addr + 1;
            test_addr <= test_addr +1;
        end
    end
end

// Ten "feature mask"

pseudo_linear_0 PL0(
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[0]),
    .y(label[0]),
    .threshold(4'd2),
    .pm(p0)
);

pseudo_linear_1 PL1 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[1]),
    .y(label[1]),
    .threshold(4'd2),
    .pm(p1)
);  

pseudo_linear_2 PL2 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[2]),
    .y(label[2]),
    .threshold(4'd2),
    .pm(p2)
);  

pseudo_linear_3 PL3 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[3]),
    .y(label[3]),
    .threshold(4'd2),
    .pm(p3)
);  

pseudo_linear_4 PL4 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[4]),
    .y(label[4]),
    .threshold(4'd2),
    .pm(p4)
);  

pseudo_linear_5 PL5 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[5]),
    .y(label[5]),
    .threshold(4'd2),
    .pm(p5)
);  

pseudo_linear_6 PL6 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[6]),
    .y(label[6]),
    .threshold(4'd2),
    .pm(p6)
);  

pseudo_linear_7 PL7 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[7]),
    .y(label[7]),
    .threshold(4'd2),
    .pm(p7)
);  

pseudo_linear_8 PL8 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[8]),
    .y(label[8]),
    .threshold(4'd2),
    .pm(p8)
);  

pseudo_linear_9 PL9 (
    .clk(clk),
    .rst_n(rst_n),
    .image_data(train_image_data),
    .result(train_result[9]),
    .y(label[9]),
    .threshold(4'd2),
    .pm(p9)
);  


//Initialise the Image RAM that contains the test image data
Image_RAM_test test_Image(
    .clk(clk),
    .we(we),
    .en(en),
    .addr(test_addr),
    .dout(test_image_data)
);

assign test_result[0] = forward(test_image_data,p0,4'd2);
assign test_result[1] = forward(test_image_data,p1,4'd2);
assign test_result[2] = forward(test_image_data,p2,4'd2);
assign test_result[3] = forward(test_image_data,p3,4'd2);
assign test_result[4] = forward(test_image_data,p4,4'd2);
assign test_result[5] = forward(test_image_data,p5,4'd2);
assign test_result[6] = forward(test_image_data,p6,4'd2);
assign test_result[7] = forward(test_image_data,p7,4'd2);
assign test_result[8] = forward(test_image_data,p8,4'd2);
assign test_result[9] = forward(test_image_data,p9,4'd2);






//forward model
function forward;
    input [783:0] test_image;
    input [783:0] p;
    input [3:0] threshold;
    reg [783:0] bitvec;
    reg [9:0] num_p,num;
    integer i,j;
    begin
    num=0;
    num_p=0;
    bitvec = p & test_image;
    for (j =0; j <784 ; j=j+1) begin //Calculate the number of "1"s in the resulting bitvec   
        num=bitvec[j] ? num+1 : num;
    end 
    for (i = 1; i<784 ; i=i+1) begin //Calculate the number of "1"s in the parameter
        num_p= p[i] ? num_p+1 : num_p;
    end  
        
    if(((num_p >> threshold))>= num) //Threshold value
        begin
            forward = 1'b1;            
        end
        else begin
            forward = 0;   
        end
    end    
endfunction
















endmodule