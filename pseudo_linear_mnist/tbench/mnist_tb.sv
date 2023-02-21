`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/01/04 00:42:38
// Design Name: 
// Module Name: mnist_tb
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


module mnist_tb();
        bit clk;
        logic rst_n;
        logic [13:0] x; //input data
        logic y;
        logic result;
        logic [784:0] captureData; // The training data from mnist data set.
        localparam period = 20;
        real accuracy;
        //instantiate the design
        pseudo_linear pl(
            .clk(clk),
            //.x(x),
            //.y(y),
            .rst_n(rst_n),
            .result(result)
        );

    // Read minits data for training from mnist_train.txt
task Read_train_data();
    int fd; // Integer variable to hold the file descriptor
    int scan_file;//file handler
    int j;
    fd = $fopen("mnist_train.txt", "r");
    if (fd) $display("Trianing FIle was opened successfully : %0d", fd );
    else     $display("Trianing FIle was NOT opened successfully : %0d", fd );
    //Read data in each line and convert the parameters to 0 and 1
    while (!$feof(fd)) begin
        scan_file = $fscanf(fd, "%b\n", captureData);// Read a single line into variable "line"
        x=j;
        j=j+1;
        @(posedge clk);
    end
endtask 

task Read_train_output();
    int fd; // Integer variable to hold the file descriptor
    int scan_file;//file handler
    int j;
    fd = $fopen("mnist_train.txt", "r");
    if (fd) $display("Trianing FIle was opened successfully : %0d", fd );
    else     $display("Trianing FIle was NOT opened successfully : %0d", fd );
    //Read data in each line and convert the parameters to 0 and 1
    while (!$feof(fd)) begin
        @(posedge clk);
        scan_file = $fscanf(fd, "%b\n", captureData);// Read a single line into variable "line"
        y=captureData[0];
        
    end
endtask 


    // Read minits test data for training from mnist_train.txt
task Read_test_data();
    int fd; // Integer variable to hold the file descriptor
    int scan_file;//file handler
    int i;
    fd = $fopen("mnist_test.txt", "r");
    if (fd) $display("Test FIle was opened successfully : %0d", fd );
    else     $display("Test FIle was NOT opened successfully : %0d", fd );
    //Read data in each line and convert the parameters to 0 and 1
    while (!$feof(fd)) begin
        scan_file = $fscanf(fd, "%b\n", captureData);// Read a single line into variable "line"
            x = i;
            y = 1'bx;
            i=i+1;
            if(result == captureData[0]) begin
                accuracy = accuracy+1;
            end
            @(posedge clk);
    end
    $display ("Model accuracy is:" , (accuracy/2115)*100);
endtask 

    always #(period/2) clk =~clk;// Generate a clock.
    // reset
    task initial_reset();
        rst_n =0;
        #80
        rst_n =1;
    endtask


    initial begin
        initial_reset();
        #10;
        // Read_test_data();
        // x=5'b10001;
        // #20
        // x=5'b10010;
        // y=0;
    end


endmodule
