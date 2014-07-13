/*
     .k8GOGGNqkSFS5XkqXPSkSkkqXXFS5kSkSS15U22F2515U2uujuu1U1u2U1U2uUuFS.     
   :0qE     JS5uuJuuFFX51jU2SSk12jU2SSXF5uuu15SFS5k12ujj21S5kFS5S12jJYu11    
  5XS:        1UYYLu.   vUUX    U22r     SUF         SUF           ;YYLuU5   
 1F5i  NNSkS7  2uLJui   51u     S5.      .PX         .XX           LJvLLu1.  
 kUk  0iLk5FFu vuYY2:   5F    Xkk7        78    E0    i0    GEXPXk2uLLvLLuk  
X25, 8O   2kX0  5YJUi   M    555    PkXk   i    q1FU   7    ONNkP12YLvLvLYS  
S25  8888  888  5uY5         FuS    PS50   .    FuUU   7          uJvLvLLJ2i 
kUF             SJjU.      P02UF    P25k   .    Su2Y   v          2LLvLvLL17 
S21  XJj88  0u  1uY2.        X2k           .    k11E   v    7;ii:JuJvLvLvJ2: 
2257 jqv   Pqq  1LJur         PP.          7    EX:    q    OqqXP51JYvLvYYS.  
 X2F  kXkXSXk  kJYLU:   O     ,Z    0PXZ   i    ii    q0    i:::,,.jLLvLLuF'  
 ik1k  ;qkPj  .uJvYu:   UN      :   XU2F   :         S5S           iJLLvjUF8   
  :PSq       72uLLLui   uSi    .;   2uY1   r.       72j1           LYYLYJSU88
    XqE2   rP12juJuu1FX55U5FqXXSXkXF1juUkkPSXSPXPXPF1Jju5FkFSFXFSF5uujUu5j28V 
      .uGOZESS5S5SFkkPkPkXkPXqXPXqXXFkSkkPXPXPkqSkSS1521252121U2u2u12Suv7   

*
* KADE - Kick Ass Dynamic Encoder
*
* Copyright (c) 2014
* Jon Wilson    - degenatrons@gmail.com
* Bruno Freitas - bootsector@ig.com.br
* Kevin Mackett - kevin@sharpfork.com
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program. If not, see <http://www.gnu.org/licenses/>.
*
* ADDITIONAL TERMS per GNU GPL Section 7
* No trademark or publicity rights are granted. This license does NOT give you 
* any right, title or interest in the KADE brand. You may not distribute any 
* modification of this program using the KADE name or KADE logo or claim any 
* affiliation or association with KADE or the KADE development team.
*
* Any propagation or conveyance of this program must include this copyright 
* notice and these terms.
*
* You may not misrepresent the origins of this program; modified versions of the 
* program must be marked as such and not identified as the original program.
*/ 

#include "USBVirtuaStick.h"
#define CPU_PRESCALE(n)	(CLKPR = 0x80, CLKPR = (n))

uint8_t old_tbX=0, old_tbX_pinc, old_tbX_pind;
uint8_t old_tbY=0, old_tbY_pinc, old_tbY_pind;
uint8_t old_tbZ=0, old_tbZ_pinc, old_tbZ_pind;
uint8_t tb=0;
uint8_t update_cycles = 0;

uint8_t centering = 1;
uint8_t sensitivity = 10;
uint8_t resistance = 1;

int16_t xAxis = 0;

void center()
{
	if (centering==1&&update_cycles==0)
	{
		if (gamepad_state.l_x_axis < 128)
		{
			gamepad_state.l_x_axis += resistance;
		}
		else if (gamepad_state.l_x_axis > 128)
		{
			gamepad_state.l_x_axis -= resistance;
		}
	}
}

int main(void) 
{
	// Set clock @ 16Mhz
	CPU_PRESCALE(0);		

	//Set initial pin states.
    DDRB=0x00;
    DDRC=0x00;
    DDRD=0x00;
    PORTB=0xFF;
    PORTC=0xFF;
    PORTD=0xFF;
		
	// Init USB pad emulation
	vs_init(true);

	//initial values for axis
	gamepad_state.l_x_axis=128;
	gamepad_state.l_y_axis=128;
	gamepad_state.r_x_axis=128;
	gamepad_state.r_y_axis=128;

	old_tbX_pinc = PINC; old_tbX_pind = PIND;
	old_tbY_pinc = PINC; old_tbY_pind = PIND;
	old_tbZ_pinc = PINC; old_tbZ_pind = PIND;
	
	// Pins polling and gamepad status updates
	while (true)
	{
		vs_reset_watchdog();				
		//set default button states - reset direction to centre
		gamepad_state.direction=8;
		gamepad_state.square_btn=0x00;
		gamepad_state.cross_btn=0x00;
		gamepad_state.circle_btn=0x00;
		gamepad_state.triangle_btn=0x00;
		gamepad_state.l1_btn=0x00;
		gamepad_state.r1_btn=0x00;					
		gamepad_state.l2_btn=0x00;
		gamepad_state.r2_btn=0x00;
		gamepad_state.l3_btn=0x00;
		gamepad_state.r3_btn=0x00;
		gamepad_state.square_axis=0x00;
		gamepad_state.cross_axis=0x00;
		gamepad_state.circle_axis=0x00;
		gamepad_state.triangle_axis=0x00;
		gamepad_state.l1_axis=0x00;
		gamepad_state.r1_axis=0x00;
		gamepad_state.l2_axis=0x00;
		gamepad_state.r2_axis=0x00;
		gamepad_state.select_btn=0x00;
		gamepad_state.start_btn=0x00;
		gamepad_state.ps_btn=0x00;		

		//HWB switches the auto-centering and resistance
		if (!(PIND&0x80))
		{
			centering = 0;
		} 
		else 
		{
			centering = 1;
		}

		//X Axis - Read quadrative state from pins A1 and A2
		if(!(old_tbX_pinc&0x04) != !(PINC&0x04) || !(old_tbX_pind&0x01) != !(PIND&0x01) )
		{		
			tb = 0;
			if (!(PINC&0x04)){ tb += 1; }
			if (!(PIND&0x01)){ tb += 2; }
			
			//Set X Axis
			if ( 	((tb==0)&&(old_tbX==2)) || 
					((tb==1)&&(old_tbX==0)) || 
					((tb==3)&&(old_tbX==1)) || 
					((tb==2)&&(old_tbX==3)) )
			{
				//Cast to a 16bit int so don't get interger overflow
				xAxis = (int16_t)gamepad_state.l_x_axis + (int16_t)sensitivity;
				
			    //Increase X Axis Position
				if (xAxis <= 255) 
				{ 
					gamepad_state.l_x_axis = xAxis;
				}
				else
				{
					//else set the xAxis to the max
					gamepad_state.l_x_axis = 255;
				}
			}
			else if ( 	((tb==0)&&(old_tbX==1)) || 
						((tb==2)&&(old_tbX==0)) || 
						((tb==3)&&(old_tbX==2)) || 
						((tb==1)&&(old_tbX==3)) )
			{
				//Cast to a 16bit int so don't get interger underflow
				xAxis = (int16_t)gamepad_state.l_x_axis - (int16_t)sensitivity;
				
			     //Decrease X Axis Position
				if (xAxis >= 0) 
				{
					gamepad_state.l_x_axis = xAxis; 
				}
				else
				{
					//else set the xAxis to the min
					gamepad_state.l_x_axis = 0;
				}
			}
			else if ( ((tb==1)&&(old_tbX==2)) || ((tb==2)&&(old_tbX==1)) || ((tb==3)&&(old_tbX==0)) || ((tb==0)&&(old_tbX==3)) )
			{
				//center();
			}
			
			old_tbX = tb;
			old_tbX_pinc = PINC; 
			old_tbX_pind = PIND;
		} 
		else 
		{
			center();
		}		
		
		//send inputs every x cycles
		update_cycles += 1;
		if (update_cycles > 3)
		{
			//digital buttons
			if(!(PINB&0x04)) { gamepad_state.square_btn=0xff; }	//PIN B1
			if(!(PINB&0x08)) { gamepad_state.cross_btn=0xff; }		//PIN B2
			if(!(PINB&0x10)) { gamepad_state.circle_btn=0xff; }	//PIN B3
			if(!(PINB&0x20)) { gamepad_state.triangle_btn=0xff; }	//PIN B4
			if(!(PINB&0x40)) { gamepad_state.l1_btn=0xff; } 		//PIN B5
			if(!(PINB&0x80)) { gamepad_state.r1_btn=0xff; } 		//PIN B6
			if(!(PINC&0x80)) { gamepad_state.l2_btn=0xff; } 		//PIN B7
			if(!(PINC&0x40)) { gamepad_state.r2_btn=0xff; } 		//PIN B8
			if(!(PINC&0x20)) { gamepad_state.select_btn=0xff; }	//PIN B9
			if(!(PINC&0x10)) { gamepad_state.start_btn=0xff; } 	//PIN B10
		
			vs_send_pad_state();
			update_cycles = 0;
		}
		_delay_ms(0.1);
	}
}
