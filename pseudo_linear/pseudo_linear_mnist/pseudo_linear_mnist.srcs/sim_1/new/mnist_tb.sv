`timescale 1ns / 1ns
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
        logic rstn;
        logic [783:0] x;
        logic y;
        logic result;
        localparam period = 20;
        //instantiate the design
        pseudo_linear pl(
            .clk(clk),
            .x(x),
            .y(y),
            .rstn(rstn),
            .result(result)
        );

        always #(period/2) clk =~clk;// Generate a clock.
        // reset
        task initial_reset();
            rstn =0;
            #100
            rstn =1;
        endtask

        initial begin
            initial_reset();
            x=200'habc183929129128192;
            y=1;
            #50
            x=200'hefe1839232323123212;
            y=0;
        end

endmodule
