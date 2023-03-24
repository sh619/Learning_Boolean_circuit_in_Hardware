`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/02/21 16:14:25
// Design Name: 
// Module Name: mnist_ten_tb
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


module mnist_ten_tb();
    bit clk;
    logic rst_n;
    logic [9:0] train_result;
    logic [9:0] test_result;
    logic [9:0] captureData;
    real accuracy;
    localparam period = 20;
    //instantiate the design
    mnist_ten pl(
        .clk(clk),
        .rst_n(rst_n),
        .train_result(train_result),
        .test_result(test_result)
    );

    task Read_test_data();
    int fd; // Integer variable to hold the file descriptor
    int scan_file;//file handler
    int i;
    fd = $fopen("final_test_label.txt", "r");
    if (fd) $display("Test FIle was opened successfully : %0d", fd );
    else     $display("Test FIle was NOT opened successfully : %0d", fd );
    //Read data in each line and convert the parameters to 0 and 1
    // for ( i=0 ; i <2048; i++ ) begin
    //     scan_file = $fscanf(fd, "%b\n", captureData);// Read a single line into variable "line"
    //     if(test_result == captureData) begin
    //         accuracy = accuracy+1;
    //     end
    // end
    while (!$feof(fd)) begin
        scan_file = $fscanf(fd, "%b\n", captureData);// Read a single line into variable "line"
        i=i+1;
        $display("label is:",captureData," test result:",test_result);

        if(test_result == captureData) begin
            accuracy = accuracy+1;
        end
        @(posedge clk);
    end
    $display ("Model accuracy is:" , (accuracy/2047)*100);
endtask 
    

    // reset
    task initial_reset();
        rst_n =0;
        #80
        rst_n =1;
    endtask
    always #(period/2) clk =~clk;// Generate a clock.
    initial begin
        initial_reset();
        #10;
        Read_test_data();
    end
endmodule
