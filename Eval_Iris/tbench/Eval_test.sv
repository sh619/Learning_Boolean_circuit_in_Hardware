`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2022/11/30 15:45:12
// Design Name: 
// Module Name: Eval_test
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


module Eval_test();

    bit clk;
    logic rst_n;
    logic [3:0] x;
    logic y;
    logic prediction;
    logic [15:0] p;
    logic [4:0] captureData; // The training data from Iris data set.
    logic [15:0] trained_p;
    localparam period = 20;
    //instantiate the design
    Eval_Iris iris(
        .clk(clk),
        .x(x),
        .y(y),
        .rst_n(rst_n),
        .prediction(prediction),
        .p(p)
    );
    // reset
    task initial_reset();
        rst_n =0;
        #100
        rst_n =1;
    endtask
     // Read Iris data for training from Iris_train.txt
    task Read_train_data();
        int fd; // Integer variable to hold the file descriptor
        int scan_file;//file handler
        fd = $fopen("Iris_train.txt", "r");
        if (fd) $display("Trianing FIle was opened successfully : %0d", fd );
        else     $display("Trianing FIle was NOT opened successfully : %0d", fd );
        //Read data in each line and convert the parameters to 0 and 1
        while (!$feof(fd)) begin
            @(posedge clk)
            scan_file = $fscanf(fd, "%b\n", captureData);// Read a single line into variable "line"
            x=captureData[4:1];
            y=captureData[0];
        end
    endtask 
    // Read Iris data for inference from Iris_train.txt
        task Read_inference_data();
        int fd; // Integer variable to hold the file descriptor
        int scan_file;//file handler
        int pre;//The inference output
        real result;
        int i;
        fd = $fopen("Iris_bi.txt", "r");
        if (fd) $display("test FIle was opened successfully : %0d", fd );
        else     $display("test FIle was NOT opened successfully : %0d", fd );
        //Read data in each line and convert the parameters to 0 and 1
        while (!$feof(fd)) begin
            scan_file = $fscanf(fd, "%b\n", captureData);// Read a single line into variable "line"
            pre=trained_p[captureData[4:1]];
            if (pre == captureData[0]) result = result+1;
            i++;
        end
        // Output the model prediction and calculate the prediction accuracy.
        $display("The model accuracy after 20 test data is : %0f" , result*100/100,"\%" );
    endtask 
    
    always #(period/2) clk =~clk;
    //reset and set clock cycle
    
    initial begin
        initial_reset();
        Read_train_data();
        x=4'hx;
        #200
        trained_p=p;
        $display("The trained parameter is :%0b" ,trained_p);
        Read_inference_data();
    end
endmodule
    