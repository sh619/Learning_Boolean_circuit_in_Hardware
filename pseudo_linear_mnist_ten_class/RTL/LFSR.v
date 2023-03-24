module LFSR #(
   parameter N=14
) (
    input clk,
    input rst_n,
    output [1:N] Q
);
    reg [1:N]  Q_reg,Q_next ;
    wire taps;

    always @(posedge clk or negedge rst_n) begin
        if(!rst_n) 
            Q_reg <= 6'd1;
        else 
            Q_reg <= Q_next;
    end

    //Next state logic
    always@(*)
        Q_next ={taps, Q_reg[1:N - 1] };
    

    //N=14
    assign taps = Q_reg[14] ^ Q_reg[13] ^ Q_reg[12] ^ Q_reg[2];

    //ouput logic
    assign Q = Q_reg;

endmodule