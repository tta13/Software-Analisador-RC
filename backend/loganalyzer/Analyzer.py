class Analyzer:

    def __init__(self, game):

        self.game = game
        self.play_on_cycles = game.get_play_on_cycles()
        self.pass_status = 0  # 0 --> no kick,  1 --> one kicker detected
        self.shoot_status = 0
        self.last_shooter = 'not'
        self.pass_last_kicker = -1
        self.pass_last_kick_cycle = -1
        self.i = 0
        self.ball_owner = 0

        # Right TEAM
        self.status_r = 0  # Winner' 'Loser' 'Draw'
        self.pass_r = 0
        self.intercept_r = 0
        self.pass_accuracy_r = 0
        self.on_target_shoot_r = 0
        self.off_target_shoot_r = 0
        self.shoot_accuracy_r = 0
        self.score_r = 0
        self.scorers_r = []
        self.possession_r = 0
        self.offsides_r = 0
        self.fouls_r = 0
        self.corners_r = 0
        self.used_stamina_agents_r = []
        self.team_moved_distance_r = []
        self.used_per_distance_r = []
        self.average_stamina_10p_r = 0
        self.average_distance_10p_r = 0
        self.av_st_per_dist_10p_r = 0

        # Left TEAM
        self.status_l = 0  # Winner' 'Loser' 'Draw'
        self.pass_l = 0
        self.intercept_l = 0
        self.pass_accuracy_l = 0
        self.on_target_shoot_l = 0
        self.off_target_shoot_l = 0
        self.shoot_accuracy_l = 0
        self.score_l = 0
        self.scorers_l = []
        self.possession_l = 0
        self.offsides_l = 0
        self.fouls_l = 0
        self.corners_l = 0
        self.used_stamina_agents_l = []
        self.team_moved_distance_l = []
        self.used_per_distance_l = []
        self.average_stamina_10p_l = 0
        self.average_distance_10p_l = 0
        self.av_st_per_dist_10p_l = 0

    def line_intersection(self,line1, line2):
        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]
        
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
        div = det(xdiff, ydiff)
        if div == 0:
           raise Exception('lines do not intersect!')
        d = (det(*line1), det(*line2))
        x = det(d, xdiff) / div
        y = det(d, ydiff) / div
        return x, y
    
    def update_distance(self, key):
        
        def distance(p1,p2):
            return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
        
        if(key in self.play_on_cycles and (key-1) in self.play_on_cycles):
            for agent in (self.game.right_team.agents + self.game.left_team.agents):
                p1 = (agent.data[key-1]['x'],agent.data[key-1]['y'])
                p2 = (agent.data[key]['x'],agent.data[key]['y'])
                agent.moved_distance = agent.moved_distance +distance(p1,p2)
        
                
    def update_parameters(self):
        
        if(self.game.left_goal == self.game.right_goal ):
            self.status_l = "Draw"
            self.status_r = "Draw"
        elif(self.game.left_goal > self.game.right_goal ):
            self.status_l = "Winner"
            self.status_r = "Loser"
        else:
            self.status_r = "Winner"
            self.status_l = "Loser"
        
        for agent in self.game.right_team.agents:
            
            agent.used_stamina = self.game.server_param['stamina_max']+self.game.server_param['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina']
            self.used_stamina_agents_r.append((round(agent.used_stamina,2),agent.number))       
            
            self.team_moved_distance_r.append((round(agent.moved_distance,2),agent.number))
            if(agent.moved_distance !=0):
                self.used_per_distance_r.append((round(agent.used_stamina/agent.moved_distance,1),agent.number))
            
            
        for agent in self.game.left_team.agents:
            
            agent.used_stamina = self.game.server_param['stamina_max']+self.game.server_param['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina_capacity']-agent.data[self.game.get_play_on_cycles()[-1]]['stamina']
            self.used_stamina_agents_l.append((round(agent.used_stamina,2),agent.number))       
    
            self.team_moved_distance_l.append((round(agent.moved_distance,2),agent.number))
            if(agent.moved_distance !=0):
                self.used_per_distance_l.append((round(agent.used_stamina/agent.moved_distance,1),agent.number))

        if(self.pass_r+self.intercept_l != 0):
            self.pass_accuracy_r  = round(self.pass_r * 100/(self.pass_r+self.intercept_l),1)
        else:
            self.pass_accuracy_r  = 0
            
        if(self.pass_l+self.intercept_r != 0):
            self.pass_accuracy_l  = round(self.pass_l * 100/(self.pass_l+self.intercept_r),1)
        else:
            self.pass_accuracy_l  = 0
            
        if(self.on_target_shoot_l+self.off_target_shoot_l != 0):
            self.shoot_accuracy_l = round(self.on_target_shoot_l *100/(self.on_target_shoot_l+self.off_target_shoot_l),1)
        else:
            self.shoot_accuracy_l  = 0
            
        if(self.on_target_shoot_r+self.off_target_shoot_r != 0):
            self.shoot_accuracy_r = round(self.on_target_shoot_r *100/(self.on_target_shoot_r+self.off_target_shoot_r),1)
        else:
            self.shoot_accuracy_r  = 0
            
        total                 = self.possession_r+self.possession_l
        if(total!=0):
            self.possession_r     = round(self.possession_r * 100 /(total) ,1)
            self.possession_l     = round(self.possession_l * 100 /(total) ,1)
        else:
            self.possession_r     = 0
            self.possession_l     = 0
        
        self.average_distance_10p_r = round(sum([d[0] for d in self.team_moved_distance_r if d[1]!=1])/10,1)
        self.average_distance_10p_l = round(sum([d[0] for d in self.team_moved_distance_l if d[1]!=1])/10,1)
        self.average_stamina_10p_r = round(sum([d[0] for d in self.used_stamina_agents_r if d[1]!=1])/10,1)
        self.average_stamina_10p_l = round(sum([d[0] for d in self.used_stamina_agents_l if d[1]!=1])/10,1)

        if(self.average_distance_10p_r !=0):
            self.av_st_per_dist_10p_r  = round(self.average_stamina_10p_r/self.average_distance_10p_r,1)
        
        if(self.average_distance_10p_l !=0):
            self.av_st_per_dist_10p_l  = round(self.average_stamina_10p_l/self.average_distance_10p_l,1)

    def update_possession(self, key):
        if key not in self.play_on_cycles:
            return

        ball_owner = self.game.get_ball_owner(key)
        if ball_owner is not None:
            if(ball_owner.team.name == self.game.left_team.name ):
                self.possession_l +=1
            else:
                self.possession_r +=1

        
    def check_shoot(self, key):

        if key in self.game.ball_pos:
            if(key not in self.play_on_cycles):
                self.shoot_status = 0
                
            elif((self.game.ball_pos[key]['Vx']**2 + self.game.ball_pos[key]['Vy']**2)** 0.5  > self.game.server_param['ball_speed_max'] * self.game.server_param['shot_threshold'] ):
                kickers = self.game.get_kickers(key)
                if(len(kickers)>0 and kickers[0].team.name == self.game.right_team.name and kickers[0].data[key]['x'] < 0 and self.game.ball_pos[key]['Vx']):
                    ball1 = (self.game.ball_pos[key-1]['x'], self.game.ball_pos[key-1]['y'])
                    ball2 = (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                    if ball1[0]-ball2[0]>0:
                        (x_right, y_right) = self.line_intersection((ball1,ball2), ((-53.0,1),(-53.0,0)))

                        # print(f'Possible shot: {key}, r_{kickers[0].number} - (x:{x_right},y:{y_right})')
                            
                        if 7.5 < abs(y_right) < 17.5:
                            self.off_target_shoot_r +=1
                            self.shoot_status       =1
                            # print(f'Shot detected:  {key}, r_{kickers[0].number}')
                            self.last_shooter = kickers[0]
                        elif abs(y_right) <= 7.5:
                            self.on_target_shoot_r +=1
                            self.shoot_status       =1
                            # print(f'On target shot detected:  {key}, r_{kickers[0].number}')  
                            self.last_shooter = kickers[0]                                        
                            
                elif(len(kickers)>0 and kickers[0].team.name == self.game.left_team.name and kickers[0].data[key]['x'] > 0 and self.game.ball_pos[key]['Vx']):
                    ball1= (self.game.ball_pos[key-1]['x'], self.game.ball_pos[key-1]['y'])
                    ball2= (self.game.ball_pos[key]['x'], self.game.ball_pos[key]['y'])
                    if ball2[0]-ball1[0]>0:
                        (x_left, y_left) = self.line_intersection((ball1,ball2), ((53.0,1),(53.0,0)))

                        # print(f'Possible shot: {key}, l_{kickers[0].number} - (x:{x_left},y:{y_left})')
    
                        if 7.5 < abs(y_left) < 17.5:
                            self.off_target_shoot_l+=1
                            self.shoot_status       =1
                            # print(f'Shot detected:  {key}, l_{kickers[0].number}')
                            self.last_shooter = kickers[0]
                        elif abs(y_left) <= 7.5:
                            self.on_target_shoot_l +=1
                            self.shoot_status       =1    
                            # print(f'On target shot detected:  {key}, l_{kickers[0].number}')
                            self.last_shooter = kickers[0]

    def check_pass(self, key):
        if len(self.game.get_last_kickers(key))>0:
            if(key not in self.play_on_cycles):
                self.pass_status = 0

            elif(self.pass_status == 0):
                self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                self.pass_last_kick_cycle = key
                self.pass_status      = 1

            elif(self.pass_status == 1):

                if(self.pass_last_kicker == self.game.get_last_kickers(key)[0] and self.game.get_last_kickers(key)[0].data[key]['is_kicked']):
                    self.pass_status = 1
                    self.pass_last_kick_cycle = key

                elif(self.pass_last_kicker != self.game.get_last_kickers(key)[0]  and  self.pass_last_kicker.team == self.game.get_last_kickers(key)[0].team):
                    self.i = self.i+1
                    if(self.pass_last_kicker.team.name == self.game.right_team.name):
                        self.pass_r += 1
                    else:
                        self.pass_l += 1                   
                        
                    self.pass_status = 1
                    self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                    self.pass_last_kick_cycle = key

                elif(self.pass_last_kicker.team != self.game.get_last_kickers(key)[0].team):
                    if(self.game.get_last_kickers(key)[0].team.name == self.game.right_team.name):
                        self.intercept_r += 1
                    else:
                        self.intercept_l += 1                
                        
                    self.pass_status = 1
                    self.shoot_status = 0
                    self.pass_last_kicker = self.game.get_last_kickers(key)[0]
                    self.pass_last_kick_cycle = key

    def update_play_mode(self, key):
        if(key in self.game.play_modes):
            split_play_mode = self.game.play_modes[key].rsplit('_')
            mode = split_play_mode[0]
            side = split_play_mode[-1]
            if(mode == 'corner'):
                if(side == 'r'):
                    self.corners_r += 1
                elif(side == 'l'):
                    self.corners_l += 1
            elif(mode == 'offside'):
                if(side == 'r'):
                    self.offsides_r += 1
                elif(side == 'l'):
                    self.offsides_l += 1
            elif(mode == 'foul'):
                if(side == 'r'):
                    self.fouls_r += 1
                elif(side == 'l'):
                    self.fouls_l += 1
            elif(mode == 'goal'):
                side = split_play_mode[1]
                if(side == 'r'):
                    self.score_r += 1
                    if(self.last_shooter.team.name == self.game.right_team.name):
                        self.scorers_r.append([key, f'{self.last_shooter.team.name}_{self.last_shooter.number}'])
                    else:
                        self.scorers_r.append([key, 'Own goal'])
                elif(side == 'l'):
                    self.score_l += 1
                    if(self.last_shooter.team.name == self.game.left_team.name):
                        self.scorers_l.append([key, f'{self.last_shooter.team.name}_{self.last_shooter.number}'])
                    else:
                        self.scorers_l.append([key, 'Own goal'])

    def analyze(self):        
        for key in range(1,self.play_on_cycles[-1]+1):
            self.check_pass(key)
            self.check_shoot(key)
            self.update_possession(key)
            self.update_distance(key)
            self.update_play_mode(key)
        self.update_parameters()