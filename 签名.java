	private String createSIG(Map<String, Object> map,String servertype){
        List<Map.Entry<String, Object>> infoIds = new ArrayList<Map.Entry<String, Object>>(map.entrySet());    
        Collections.sort(infoIds, new Comparator<Map.Entry<String, Object>>() {  
            @Override  
            public int compare(Map.Entry<String, Object> o1, Map.Entry<String, Object> o2) {  
                return (o1.getKey()).toString().compareTo(o2.getKey());  
            }  
        });
        StringBuilder buf = new StringBuilder();  
        for (Map.Entry<String, Object> item : infoIds) {  
                String key = item.getKey();  
                if(item.getValue() instanceof String){
                	buf.append(key + "=" +(String) item.getValue()); 
                }else if(item.getValue() instanceof Integer){
                	buf.append(key + "=" +(Integer) item.getValue()); 
                }else if(item.getValue() instanceof Long){
                	buf.append(key + "=" +(Long) item.getValue()); 
                }
        }
        String key="";
		if(servertype.equals(Cconfig.SERVER_TYPE_COMMUNITY)){
			key=Cconfig.COMMUNITT_SIGN_ANDROID_KEY;
		}else if (servertype.equals(Cconfig.SERVER_TYPE_LIVE)) {
			key=((String)map.get("platform")).toLowerCase().equals("android")?Cconfig.LIVE_SIGN_ANDROID_KEY:Cconfig.LIVE_SIGN_IOS_KEY;
		}
		
		String sig="";
		int key_len=key.length();
		String md5=HelperUtil.MD5(buf.toString());
		int md5_len=md5.length()/2;
		String ch;
		for(int i=0;i<md5_len;i++){
			if(!key.equals("")){
				int ch1 =Integer.parseInt((md5.charAt(i*2)+"")+(md5.charAt(i*2+1)+""),16);
				int ch2= Integer.valueOf(key.charAt(i%key_len));
				ch=(ch1^ch2)+"";
			//	System.out.println("ch1="+ch1+",ch2="+ch2+",ch="+ch);
			}else{
				if(HelperUtil.isNumber(md5.charAt(i)+"")){
					ch= Integer.parseInt(md5.charAt(i)+"")+"";
				}else{
					ch="0";
				}
			}
			ch=Integer.toHexString(Integer.parseInt(ch));
			if(ch.length()==1){
				ch="0"+ch;
			}
			//System.out.println("ch="+ch);
			sig=sig+ch;
		}
		logger.info("sig="+sig+",md5="+md5+",string="+buf.toString());
		return sig;
	}